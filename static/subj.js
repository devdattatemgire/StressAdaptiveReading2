
document.addEventListener("DOMContentLoaded", function() {
    const openHelloButton = document.getElementById("re_sci");

    openHelloButton.addEventListener("click", function() {
        window.location.href = "sci.html";
    });
});



document.addEventListener("DOMContentLoaded", function() {
    const openHelloButton = document.getElementById("re_geo");

    openHelloButton.addEventListener("click", function() {
        window.location.href = "geo.html";
    });
});

function changeButtonColor(buttonNumber) {
    // Reset background color and text color for all buttons
    for (let i = 1; i <= 4; i++) {
        document.getElementById("button" + i).style.backgroundColor = "red";
        document.getElementById("button" + i).style.color = "white";
    }

    // Change background color to green and text color to white for the clicked button
    document.getElementById("button" + buttonNumber).style.backgroundColor = "green";
    document.getElementById("button" + buttonNumber).style.color = "white";
}



document.addEventListener("DOMContentLoaded", function() {
    const openHelloButton = document.getElementById("re_his");

    openHelloButton.addEventListener("click", function() {
        window.location.href = "his.html";
    });
});


function redirectToDM(targetURL) {
    // Redirect to the desired URL
    window.location.href = targetURL;
}

// function changeButtonColor(buttonNumber) {
//     var buttons = document.querySelectorAll('.button');
//     var clickedButton = buttons[buttonNumber - 1];

//     // Reset all button colors to default
//     buttons.forEach(function (button) {
//         button.style.backgroundColor = '';
//         button.style.color = '';
//     });

//     // Set the clicked button to green background and white text
//     clickedButton.style.backgroundColor = 'green';
//     clickedButton.style.color = 'white';
// }

// var buttons = document.querySelectorAll('.button');
// var isAnswered = false;

// function changeButtonColor(buttonNumber, isCorrect) {
//     if (!isAnswered) {
//         isAnswered = true;
//         buttons.forEach(function (button, index) {
//             if (index === buttonNumber - 1 ) 
//             {
//                 if (isCorrect) {
//                     button.style.backgroundColor = 'green';
//                     button.style.color = 'white';
//                 } 
//                 button.style.backgroundColor = 'red';
//                 button.style.color = 'white';
//                 // else {
                 
//                 //     button.style.backgroundColor = 'red';
//                 //     button.style.color = 'white';
//                 // }
//             } 
//             else {
//                 button.style.backgroundColor = 'red';
//                 button.style.color = 'white';
//             }
//             button.disabled = true; // Disable all buttons after user makes a choice
//         });
//     }
// }

var buttons = document.querySelectorAll('.button');
var isAnswered = false;

function changeButtonColor(buttonNumber, isCorrect) {
    if (!isAnswered) {
        isAnswered = true;
        buttons.forEach(function (button, index) {
            if (index === buttonNumber - 1 && isCorrect===true ) 
            {
               
                    button.style.backgroundColor = 'green';
                    button.style.color = 'white';

                
            } 
            else {
                button.style.backgroundColor = 'red';
                button.style.color = 'white';
            }
            button.disabled = true; // Disable all buttons after user makes a choice
        });
    }
}

function changeButtonColor(buttonNumber, isCorrect) {
    if (!isAnswered) {
        isAnswered = true;
        buttons.forEach(function (button, index) {
            if (index === buttonNumber - 1 && isCorrect===true ) 
            {
               
                    button.style.backgroundColor = 'green';
                    button.style.color = 'white';

                
            } 
            else {
                button.style.backgroundColor = 'red';
                button.style.color = 'white';
            }
            button.disabled = true; // Disable all buttons after user makes a choice
        });
    }
}

