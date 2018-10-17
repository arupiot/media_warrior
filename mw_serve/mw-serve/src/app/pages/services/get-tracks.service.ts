import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GetTracksService {
  constructor(private httpClient: HttpClient) { }
  getTracks()
  {
    return this.httpClient.get('http://' + window.location.hostname + ':5002/get-track-list');
  }
  getSingleTrack(id)
  {
    return this.httpClient.get('http://' + window.location.hostname + ':5002/get-single-track?id=' + id);
  }
}
