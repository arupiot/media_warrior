import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { TrackSelectorComponent } from './pages/track-selector/track-selector.component';
import { TrackComponent } from './pages/track-selector/components/track/track.component';

import {AppRoutingModule } from './app-routing.module';
import { SplashScreenComponent } from './pages/splash-screen/splash-screen.component';
import { TrackControlComponent } from './pages/track-control/track-control.component';

@NgModule({
  declarations: [
    AppComponent,
    TrackSelectorComponent,
    TrackComponent,
    SplashScreenComponent,
    TrackControlComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
