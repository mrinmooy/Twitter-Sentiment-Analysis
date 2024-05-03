import { Component } from '@angular/core';
import { HttpClientModule, HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-send-tweets',
  standalone: true,
  imports: [HttpClientModule],
  templateUrl: './send-tweets.component.html',
  styleUrls: ['./send-tweets.component.css']
})
export class SendTweetsComponent {
  constructor(private http: HttpClient) { }

  sendTweet(tweet: string, tweetInput: HTMLTextAreaElement): void {
    const url = 'https://twitter-sentiment-analysis-flask.onrender.com/api/tweet';
    this.http.post(url, { tweet }).subscribe({
      next: (response) => {
        console.log('Response:', response);
        alert('Tweet sent successfully!');
        tweetInput.value = ''; // Clear the input box after successful operation
      },
      error: (error) => {
        console.error('Error:', error);
        alert('Failed to send tweet.');
      }
    });
  }
}
