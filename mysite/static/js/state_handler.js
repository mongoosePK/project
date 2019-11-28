/*
  This file is used to help extract the js code needed to set event handlers
  to the add buttons associated with each individaul movie.
*/

function handleLoadEvent() {
  //const newEvent = new Event("build");

  let currElement = null;
  for (let e of document.getElementsByClassName("add-btn")) {
    handleSave(e.id);
  }
}
function handleSave(currMovieId) {
  const movie = document.querySelector(`#${currMovieId}`);
  setState(movie);
  let currState = movie.clickState;
  movie.style.color = currState === "saved" ? "red":"black";
}
function setState(currMovie) {
  currMovie.clickState = currMovie.clickState === "unsaved"? "saved": "unsaved";
  handleEventListener(currMovie);
}
const handleEventListener = (currMovie) => {
  //const movieElement = document.getElementById(`${movieId}`);

  if (currMovie.clickState === "unsaved") {
    currMovie.addEventListener("mouseover", setColor);
    currMovie.addEventListener("mouseout", removeColor);
  }
  else {
    currMovie.removeEventListener("mouseover", setColor);
    currMovie.removeEventListener("mouseout", removeColor);
  }
}
function setColor() {
  this.style.color = "red";
}

function removeColor() {
  this.style.color = "black";
}
