// Function to make the text bold
function makeBold(id) {
    var element = document.getElementById(id);
    if (element) {
      element.style.fontWeight = 'bold';
    }
  }
  
  // Function to increase the font size
  function increaseFontSize(id) {
    var element = document.getElementById(id);
    if (element) {
      element.style.fontSize = '1.2em';
    }
  }
  
  // Function to make the text italic
  function makeItalic(id) {
    var element = document.getElementById(id);
    if (element) {
      element.style.fontStyle = 'italic';
    }
  }
  
  // Function to apply strikethrough
  function applyStrikethrough(id) {
    var element = document.getElementById(id);
    if (element) {
      element.style.textDecoration = 'line-through';
    }
  }
  
  // Function to apply a link to the text
function applyLink(id, url) {
    var element = document.getElementById(id);
    if (element) {
      var link = document.createElement('a');
      link.href = url; // Set the URL for the link
      link.textContent = element.textContent; // Use the text content of the span as the link text
      element.textContent = ''; // Clear the span's content
      element.appendChild(link); // Append the link to the span
    }
  }
  
  // Call the function to apply a link to the specified span element
  applyLink('link', 'https://example.com'); // Replace 'https://example.com' with the desired URL
  
  // Call the functions to modify the span elements
  makeBold('bold');
  makeBold('bold');
  increaseFontSize('big');
  makeItalic('italics');
  applyStrikethrough('strike');
  