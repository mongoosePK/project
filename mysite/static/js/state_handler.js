/*
  This file is used to help extract the js code needed to set event handlers
  to the add buttons associated with each individaul movie.
*/
let savedMovies = {};
function loadMovies() {
  sessionStorage.clear();
  sessionStorage.setItem("savedMovies", JSON.stringify(savedMovies));
  // To retrieve session storage data parse json:
  //let testData = JSON.parse(sessionStorage.getItem("savedMovies"));
}
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
  handleSavedMovie(currMovie);
}
function handleSavedMovie(currMovie) {
  switch(currMovie.clickState) {
    case "saved":
      storeSavedMovie(currMovie);
    break
    case "unsaved":
      removeSavedMovie(currMovie);
    break;
    default:
    break;
  }
}
const storeSavedMovie = (currMovie) => {
  console.log(`Storing: ${currMovie.id}`);
  savedMovies[currMovie.id] = currMovie;
}
const removeSavedMovie = (currMovie) => {
  delete savedMovies[currMovie.id];
}
function handleEventListener(currMovie) {
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
