console.log("Hello from script.js");

// What is this?
console.log(window); // this is the object that represents the entirety of the page - the entire object including all the properties that are made available through the browser.

// What is the difference between window and document?
// document is the object that contains all the html code as we've typed it in index.html
console.log(document);

// What is the difference between document and document.documentElement?
console.log(window.document); // window.document returns the same object as 'document' (document is a child of window?)
console.log(document.documentElement); // document.documentElement returns all the element tags (excludes HTML5 !DOCTYPE tag at the top) - documentElement a child of document?

// what are the children of the body element?
console.log(document.body.children); // returns an array with the children of the body element, in our case a div with a class of .container and a script element
