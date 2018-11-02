import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GetStylesService {
  pink = false;
  constructor() {}
  updateStyles() {
    this.pink = !this.pink;
  }

  getStyles() {
    return this.pink;
  }
}

