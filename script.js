const apiBaseUrl = "https://j1nsgbymw8.execute-api.ap-south-1.amazonaws.com/prod";

async function subscribe() {
  const email = document.getElementById("emailInput").value;
  try {
    const res = await fetch(`${apiBaseUrl}/subscribe`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email })
    });
    const data = await res.json();
    document.getElementById("responseMessage").innerText = data.message || "Subscribed!";
  } catch (err) {
    document.getElementById("responseMessage").innerText = "Subscription failed!";
  }
}

async function submitEvent() {
  const title = document.getElementById("eventTitle").value;
  const description = document.getElementById("eventDescription").value;
  try {
    const res = await fetch(`${apiBaseUrl}/create-event`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description })
    });
    const data = await res.json();
    document.getElementById("responseMessage").innerText = data.message || "Event created!";
  } catch (err) {
    document.getElementById("responseMessage").innerText = "Failed to create event!";
  }
}

