import { Routes } from '@angular/router';
import { S3UploaderComponent } from './file-upload/file-upload';
import { Uploader } from './uploader/uploader';

export const routes: Routes = [
  { path: '', component: Uploader },
  { path: 's3', component: S3UploaderComponent}
];
