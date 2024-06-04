document.addEventListener("DOMContentLoaded", function() {
  let stripe;
  let elements;

  document
    .querySelector("#payment-form")
    .addEventListener("submit", handleSubmit);

  fetch("/products/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
      stripe = Stripe(data.publicKey);
      fetch("/products/create-checkout-session/")
      .then((result) => { return result.json(); })
      .then((data) => {
        const clientSecret = data.clientSecret;
        document.querySelector("#client-secret").value = clientSecret;  // Set the client secret in a hidden input field
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

    // Fetch the order number from the server or session
    const orderNumber = document.querySelector("#order-number").value;

    const { error } = await stripe.confirmPayment({
      elements,
      confirmParams: {
        return_url: `https://hot-cup-a72a7710ed7c.herokuapp.com/bag/checkout_success/${orderNumber}/`,
      },
    });

    if (error) {
      showMessage(error.message);
    } else {
      showMessage("An unexpected error occurred.");
    }
    setLoading(false);
  }

  function showMessage(messageText) {
    const messageContainer = document.querySelector("#payment-message");
    messageContainer.classList.remove("hidden");
    messageContainer.textContent = messageText;
    setTimeout(function () {
      messageContainer.classList.add("hidden");
      messageText.textContent = "";
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
});