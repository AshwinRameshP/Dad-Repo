// src/app/s3-uploader.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule, HttpHeaders } from '@angular/common/http';

@Component({
  standalone: true,
  selector: 'app-s3-uploader',
  imports: [CommonModule, HttpClientModule],
  template: `
    <input type="file" (change)="onFileSelected($event)" />
    <button (click)="uploadFile()">Upload</button>
    <div *ngIf="uploadProgress > 0">Progress: {{ uploadProgress }}%</div>
  `
})
export class S3UploaderComponent {
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
      if (event.type === 1 && event.total)
        this.uploadProgress = Math.round((event.loaded / event.total) * 100);
      else if (event.type === 4)
        console.log('✅ Upload complete');
    });
  }
}