import { Component, OnInit } from '@angular/core';
import { HttpClientModule, HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-postive',
  standalone: true,
  imports: [HttpClientModule],
  templateUrl: './negative.component.html',
  styleUrl: './negative.component.css'
})
export class NegativeComponent implements OnInit {
  negativeTweets: string[] = [];
  formattedTweets: string = '';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.loadNegativeTweets();
  }

  loadNegativeTweets() {
    this.http.get<string[]>('http://localhost:5000/api/negative').subscribe({
      next: (tweets) => {
        this.negativeTweets = tweets;
        this.formatTweets();
      },
      error: (error) => {
        console.error('Error fetching negative tweets', error);
      }
    });
  }

  formatTweets() {
    this.formattedTweets = this.negativeTweets.map(tweet => `<span>${tweet}</span><br>`).join('');
  }
}
