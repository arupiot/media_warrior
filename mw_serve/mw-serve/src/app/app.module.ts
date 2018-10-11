import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { TrackSelectorComponent } from './pages/track-selector/track-selector.component';
import { TrackComponent } from './pages/track-selector/components/track/track.component';

@NgModule({
  declarations: [
    AppComponent,
    TrackSelectorComponent,
    TrackComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
