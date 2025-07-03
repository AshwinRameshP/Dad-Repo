import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { App } from './app/app';
import { S3UploaderComponent } from './app/file-upload/file-upload';

bootstrapApplication(App, appConfig)
  .catch((err) => console.error(err));
bootstrapApplication(S3UploaderComponent);

