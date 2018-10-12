import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TrackSelectorComponent } from './pages/track-selector/track-selector.component';
import { SplashScreenComponent } from './pages/splash-screen/splash-screen.component';
import { TrackControlComponent } from './pages/track-control/track-control.component';

const routes: Routes = [
  {path: 'tracks', component: TrackSelectorComponent},
  {path: 'splash', component: SplashScreenComponent},
  {path: 'control', component: TrackControlComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}