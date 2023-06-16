// Initialize the recognition instance
const recognition = new webkitSpeechRecognition();

// Function to start listening for voice input
function startListening() {
  recognition.start();
  isRecording = true;
  updateUI();
}

// Function to stop listening for voice input
function stopListening() {
  recognition.stop();
  isRecording = false;
  updateUI();
}

// Event handler for when speech recognition receives a result
recognition.onresult = function(event) {
  const recognizedText = event.results[0][0].transcript;
  const usernameInput = document.getElementById('exampleUsername');
  const passwordInput = document.getElementById('examplePassword');

  const usernameRegex = /user(?:\s+)?name(?:\s+)?is (.+)/i;
  const passwordRegex = /password is (.+)/i;

  if (usernameRegex.test(recognizedText)) {
    const username = recognizedText.match(usernameRegex)[1].replace('.', '').trim();
    usernameInput.value = username;
  } else if (passwordRegex.test(recognizedText)) {
    const password = recognizedText.match(passwordRegex)[1].replace('.', '').trim();
    passwordInput.value = password;
  }

  const recognizedTextElement = document.getElementById('recognized-text');
  recognizedTextElement.textContent = 'Recognized Text: ' + recognizedText.replace('.', '');

  if (recognizedText.toLowerCase().includes('create')) {
    document.getElementById('signupButton').click(); 
  }
};

// Event handler for when speech recognition encounters an error
recognition.onerror = function(event) {
  console.log('Speech recognition error occurred:', event.error);
};

// Function to toggle recording
let isRecording = false;

function toggleRecording() {
  if (isRecording) {
    stopListening();
  } else {
    startListening();
  }
}

// Function to update the UI based on recording state
function updateUI() {
  const microphoneIcon = document.getElementById('microphone');
  const microphoneElement = microphoneIcon.querySelector('i');

  if (isRecording) {
    microphoneElement.classList.remove('fa-microphone');
    microphoneElement.classList.add('fa-stop');
    microphoneIcon.style.backgroundColor = 'red';
  } else {
    microphoneElement.classList.remove('fa-stop');
    microphoneElement.classList.add('fa-microphone');
    microphoneIcon.style.backgroundColor = 'gray';
  }
}

// Event listener for form submission
document.getElementById('signup-form').addEventListener('submit', function(event) {
  // Prevent the form from being submitted automatically
  event.preventDefault();

  // You can add any additional validation or processing here before submitting the form using AJAX or other methods.
  // For demonstration purposes, we will log the form values to the console.
  const username = document.getElementById('exampleUsername').value;
  const password = document.getElementById('examplePassword').value;
  console.log('Username:', username);
  console.log('Password:', password);

  // Create a FormData object and append the form data
  const formData = new FormData();
  formData.append('username', username);
  formData.append('password', password);

  // Make an AJAX request to submit the form data
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/signup/');
  xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken')); // Include the CSRF token
  xhr.onload = function() {
    if (xhr.status === 200) {
      console.log('Form submitted successfully!');
      // You can perform any further actions here after the form is submitted successfully.
      window.location.href = '/';
    }
  };
  xhr.send(formData);
});

// Function to get the CSRF token from cookies
function getCookie(name) {
  const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
  return cookieValue ? cookieValue.pop() : '';
}
