/*
function smoothScrollTop (another, duration) {
  var another = document.querySelector(another)
  var targetPosition = another.getBoundingClientRect().top
  var startPosition = window.pageYOffset
  var distance = targetPosition - startPosition
  var startTime = null

  function animation (currentTime) {
    if (startTime === null) startTime = currentTime

    var timeElapsed = currentTime - startTime

    var run = ease(timeElapsed, startPosition, distance, duration)

    window.screenTo(0, null)

    if (timeElapsed < duration) requestAnimationFrame(animation)
  }

  function ease (t, b, c, d) {
    t /= d / 2
    if (t < 1) return c / 2 * t * t + b
    t--
    return -c / 2 * (t * (t - 2) - 1) + b
  }

  requestAnimationFrame(animation)
}

smoothScrollTop('.scroll-top', 1000)

*/

// var mainScrollToTop = document.querySelector('.scroll-top')

// mainScrollToTop.addEventListener('click', function () {
//   smoothScrollTop('.head-part', 1000)
// })
