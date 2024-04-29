import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SendTweetsComponent } from './send-tweets.component';

describe('SendTweetsComponent', () => {
  let component: SendTweetsComponent;
  let fixture: ComponentFixture<SendTweetsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SendTweetsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SendTweetsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
