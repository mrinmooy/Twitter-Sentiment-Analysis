import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NegativeComponent } from './negative.component';

describe('NegativeComponent', () => {
  let component: NegativeComponent;
  let fixture: ComponentFixture<NegativeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NegativeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(NegativeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
