import { Component, OnInit } from '@angular/core';
import { GetTracksService } from '../services/get-tracks.service';
import { GetStylesService } from '../services/get-styles.service';

@Component({
  selector: 'app-splash-screen',
  templateUrl: './splash-screen.component.html',
  styleUrls: ['./splash-screen.component.css']
})
export class SplashScreenComponent implements OnInit {
  constructor(
    private getTracksService: GetTracksService,
    private getStylesService: GetStylesService
  ) {}

  changeStyles() {
    this.getStylesService.updateStyles();
  }
  styleObject() {
    if (!this.getStylesService.getStyles()) {
      return {border: 'none'};
    }

  }
  ngOnInit() {}
}
