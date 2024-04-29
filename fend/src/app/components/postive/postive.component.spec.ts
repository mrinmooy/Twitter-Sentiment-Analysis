import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PostiveComponent } from './postive.component';

describe('PostiveComponent', () => {
  let component: PostiveComponent;
  let fixture: ComponentFixture<PostiveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PostiveComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(PostiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
