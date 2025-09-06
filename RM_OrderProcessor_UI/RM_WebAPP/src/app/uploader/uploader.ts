import { HttpClient, HttpClientModule, HttpEventType, HttpHeaders } from '@angular/common/http';
import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { CommonModule } from '@angular/common';



@Component({
  selector: 'app-uploader',
  standalone: true,
  imports: [
    CommonModule,
    HttpClientModule,
    MatCardModule,
    MatToolbarModule,
    MatButtonModule,
    MatProgressBarModule
  ],
  templateUrl: './uploader.html',
  styleUrl: './uploader.css'
})
export class Uploader {
selectedFile!: File;
  uploadProgress = 0;

  constructor(private http: HttpClient) {}

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (!input.files?.length) return;
    this.selectedFile = input.files[0];
  }

  uploadFile() {
    const bucketUrl = 'https://rm-purchase-order-input.s3.ap-south-1.amazonaws.com';
    const uploadUrl = `${bucketUrl}/${encodeURIComponent(this.selectedFile.name)}`;
    const headers = new HttpHeaders({ 'Content-Type': this.selectedFile.type });

    this.http.put(uploadUrl, this.selectedFile, {
      headers,
      reportProgress: true,
      observe: 'events'
    }).subscribe(event => {
      if (event.type === HttpEventType.UploadProgress && event.total) {
        this.uploadProgress = Math.round((event.loaded / event.total) * 100);
      } else if (event.type === HttpEventType.Response) {
        console.log('✅ Upload complete');
      }
    });
  }
}
