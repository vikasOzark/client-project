"use strict";

const MarqueeTopBottom = (selector, speed) => {
  const parentSelector = document.querySelector(selector);
  const clone = parentSelector.innerHTML;
  const firstElement = parentSelector.children[0];
  const firstElementClientWidth = firstElement.clientWidth
  let i = 0;
  let marqueeInterval;
  
  parentSelector.insertAdjacentHTML('beforeend', clone);
  parentSelector.insertAdjacentHTML('beforeend', clone);
  const startMarquee = () => {
    marqueeInterval = setInterval(() =>{
      firstElement.style.marginTop = `-${i}px`;
      if(i > firstElementClientWidth) {
        i = 0;
      }
      i = i + speed;
    },10)
  }
  
  
  const stopMarquee = () => {
    clearInterval(marqueeInterval);
  }
  
  parentSelector.addEventListener('mouseenter', stopMarquee);
  parentSelector.addEventListener('mouseleave', startMarquee);
  
  startMarquee();
}
  
window.addEventListener('load', () => {
  MarqueeTopBottom('.marquee-top-bottom', .4)
});

const MarqueeLeftRight = (selector, speed) => {
  const parentSelector = document.querySelector(selector);
  const clone = parentSelector.innerHTML;
  const firstElement = parentSelector.children[0];
  const firstElementClientWidth = firstElement.clientWidth
  let i = 0;
  let marqueeInterval;
  
  parentSelector.insertAdjacentHTML('beforeend', clone);
  parentSelector.insertAdjacentHTML('beforeend', clone);
  const startMarquee = () => {
    marqueeInterval = setInterval(() =>{
      firstElement.style.marginLeft = `-${i}px`;
      if(i > firstElementClientWidth) {
        i = 0;
      }
      i = i + speed;
    },10)
  }
  
  
  const stopMarquee = () => {
    clearInterval(marqueeInterval);
  }
  
  parentSelector.addEventListener('mouseenter', stopMarquee);
  parentSelector.addEventListener('mouseleave', startMarquee);
  
  startMarquee();
}
window.addEventListener('load', () => {
  MarqueeLeftRight('.marquee-left-right', .4)
});