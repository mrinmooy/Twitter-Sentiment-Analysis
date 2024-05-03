import { Component, OnInit } from '@angular/core';
import { HttpClientModule, HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-postive',
  standalone: true,
  imports: [HttpClientModule],
  templateUrl: './postive.component.html',
  styleUrl: './postive.component.css'
})
export class PositiveComponent implements OnInit {
  positiveTweets: string[] = [];
  formattedTweets: string = '';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.loadPositiveTweets();
  }

  loadPositiveTweets() {
    this.http.get<string[]>('https://twitter-sentiment-analysis-flask.onrender.com/api/positive').subscribe({
      next: (tweets) => {
        this.positiveTweets = tweets;
        this.formatTweets();
      },
      error: (error) => {
        console.error('Error fetching positive tweets', error);
      }
    });
  }

  formatTweets() {
    this.formattedTweets = this.positiveTweets.map(tweet => `<span>${tweet}</span><br>`).join('');
  }
}
