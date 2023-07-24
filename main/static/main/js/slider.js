/** @type {?HTMLDivElement} */
const slideMain = document.querySelectorAll(".slide");

let counter = 0;
slideMain?.forEach(
  (slide, index) => { 
    slide.style.left = `${index *  100}%`
})
const slideImage = () => {
  slideMain?.forEach(
    (slide) => {
      slide.style.transform = `translateX(-${counter * 100}%)`
    }
  )
  counter = (counter + 1) % slideMain.length;
}
setInterval(()=>{
  slideImage()
}, 3000)


