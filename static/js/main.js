document.addEventListener("DOMContentLoaded", function() {
  let stripe;
  let elements;

  fetch("/products/config/")
    .then((result) => result.json())
    .then((data) => {
      stripe = Stripe(data.publicKey);
      initializeStripeElements(stripe);
    })
    .catch((error) => console.error("Failed to fetch Stripe configuration:", error));

  function initializeStripeElements(stripe) {
    fetch("/products/create-checkout-session/")
      .then((result) => result.json())
      .then((data) => {
        const clientSecret = data.clientSecret;
        document.querySelector("#client-secret").value = clientSecret;
        const appearance = { theme: 'stripe' };
        elements = stripe.elements({ appearance, clientSecret });

        const paymentElementOptions = {
          layout: "tabs",
        };

        const paymentElement = elements.create("payment", paymentElementOptions);
        paymentElement.mount("#payment-element");
      })
      .catch((error) => console.error("Failed to create checkout session:", error));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);

    // Cache checkout data
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const clientSecret = document.querySelector("#client-secret").value;
    const saveInfo = Boolean(document.querySelector("#id-save-info").checked);
    const postData = {
      'csrfmiddlewaretoken': csrfToken,
      'client_secret': clientSecret,
      'save_info': saveInfo,
    };

    fetch('/bag/cache_checkout_data/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
      body: JSON.stringify(postData),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to cache checkout data');
      }
      return response.json();
    })
    .then(async () => {
      const { error } = await stripe.confirmPayment({
        elements,
        confirmParams: {
          return_url: `https://hot-cup-a72a7710ed7c.herokuapp.com/bag/checkout_success/`,
        },
      });

      if (error) {
        showMessage(error.message);
      } else {
        showMessage("An unexpected error occurred.");
      }
      setLoading(false);
    })
    .catch((error) => {
      console.error("Failed to cache checkout data:", error);
      setLoading(false);
    });
  }

  document.querySelector("#payment-form").addEventListener("submit", handleSubmit);

  function showMessage(messageText) {
    const messageContainer = document.querySelector("#payment-message");
    messageContainer.classList.remove("hidden");
    messageContainer.textContent = messageText;
    setTimeout(() => {
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
});