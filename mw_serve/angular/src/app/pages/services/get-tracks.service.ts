import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GetTracksService {
  constructor(private httpClient: HttpClient) { }

  getTracks() {
    return this.httpClient.get('http://' + window.location.hostname + '/get-track-list');
  }

  getSingleTrack(id) {
    return this.httpClient.get('http://' + window.location.hostname + '/get-single-track?id=' + id);
  }

  playSingleTrack(id) {
    return this.httpClient.get('http://' + window.location.hostname + '/play-single-track?id=' + id);
  }

  pauseSingleTrack(id) {
    return this.httpClient.get('http://' + window.location.hostname + '/pause-track?id=' + id);
  }

  stopMusic() {
    return this.httpClient.get('http://' + window.location.hostname + '/stop');
  }
}
