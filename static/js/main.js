let stripe;
let elements;

document
  .querySelector("#payment-form")
  .addEventListener("submit", handleSubmit);

// Fetch Stripe configuration and handle potential errors
fetch("/products/config/")
  .then((result) => { return result.json(); })
  .then((data) => {
    stripe = Stripe(data.publicKey);
    // Fetch checkout session details and handle potential errors
    fetch("/products/create-checkout-session/")
    .then((result) => { return result.json(); })
    .then((data) => {
      const clientSecret = data.clientSecret;
      const appearance = {theme: 'stripe'};
      elements = stripe.elements({ appearance, clientSecret });
      const paymentElementOptions = {
        layout: "tabs",
      };

      try {
        const paymentElement = elements.create("payment", paymentElementOptions);
        paymentElement.mount("#payment-element");
      } catch (error) {
        console.error("Error mounting payment elements:", error);
        showMessage("Failed to initialize payment interface. Please refresh the page and try again.");
      }
    })
    .catch(error => console.error("Failed to create checkout session:", error));
  })
  .catch(error => console.error("Failed to fetch Stripe configuration:", error));

async function handleSubmit(e) {
  e.preventDefault();
  setLoading(true);

  // Attempt to confirm the payment with Stripe and handle any potential errors
  const { error } = await stripe.confirmPayment({
    elements,
    confirmParams: {
      // The `return_url` is a critical URL where the user is redirected after the payment process.
      // This should be a live, secure endpoint on your website that handles the outcome of the payment.
      // It's used especially for payments that require user authorization away from your site (e.g., bank transfers).
      // On this page, you can display the payment status, update user records, or provide receipts.
      return_url: "https://hot-cup-a72a7710ed7c.herokuapp.com/successful",
    },
  });
  // This point will only be reached if there is an immediate error when
  // confirming the payment. Otherwise, your customer will be redirected to
  // your `return_url`. For some payment methods like iDEAL, your customer will
  // be redirected to an intermediate site first to authorize the payment, then
  // redirected to the `return_url`.
  if (error) {
    if (error.type === "card_error" || error.type === "validation_error") {
      showMessage(error.message);
    } else {
      showMessage("An unexpected error occurred.");
    }
  }

  setLoading(false);
}

// Fetches the payment intent status after payment submission and handles edge cases
async function checkStatus() {
  const clientSecret = new URLSearchParams(window.location.search).get("payment_intent_client_secret");

  if (!clientSecret) {
    return;
  }

  const { paymentIntent, error } = await stripe.retrievePaymentIntent(clientSecret);
  if (error) {
    showMessage("Failed to retrieve payment status: " + error.message);
    return;
  }

  switch (paymentIntent.status) {
    case "succeeded":
      showMessage("Payment succeeded!");
      break;
    case "processing":
      showMessage("Your payment is processing.");
      break;
    case "requires_payment_method":
      showMessage("Your payment was not successful, please try again.");
      break;
    default:
      showMessage("Something went wrong.");
      break;
  }
}

// UI helper functions
function showMessage(messageText) {
  const messageContainer = document.querySelector("#payment-message");
  messageContainer.classList.remove("hidden");
  messageContainer.textContent = messageText;

  setTimeout(function () {
    messageContainer.classList.add("hidden");
    messageContainer.textContent = "";
  }, 4000);
}

function setLoading(isLoading) {
  if (isLoading) {
    document.querySelector("#submit").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("#submit").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
}