/**
 * ============================================================
 * FRONTEND LOGIC
 * app.js
 * ============================================================
 */

const API_BASE_URL = "";

// ============================================================
// DOM REFERENCES
// ============================================================

const postListEl = document.getElementById("post-list");
const stateMessageEl = document.getElementById("state-message");

// ============================================================
// HELPERS
// ============================================================

function formatDate(utcSeconds) {
  const date = new Date(utcSeconds * 1000);
  return date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric"
  });
}

function setStateMessage(text, isError = false) {
  // 1. Mətni elementə daxil edirik
  stateMessageEl.textContent = text;
  
  // 2. Xəta vəziyyətinə görə CSS klassını tənzimləyirik
  if (isError) {
    stateMessageEl.classList.add("error");
  } else {
    stateMessageEl.classList.remove("error");
  }
  
  // 3. Əgər mətn boşdursa elementi gizlədirik, doludursa göstəririk
  if (text === "") {
    stateMessageEl.style.display = "none";
  } else {
    stateMessageEl.style.display = "";
  }
}

// ============================================================
// RENDERING
// ============================================================

function buildPostHTML(post, rank) {
  // Şablondakı tələbə əsasən tək post üçün HTML string qaytarırıq
  return `
    <li class="post-item">
      <div class="post-rank">${rank}</div>
      <div class="post-body">
        <a class="post-title" href="${post.url}" target="_blank" rel="noopener">
          ${post.title}
        </a>
        <div class="post-meta">
          <span>${post.score} points</span>
          <span>by ${post.author}</span>
          <span>${formatDate(post.created_utc)}</span>
          <a href="${post.permalink}" target="_blank" rel="noopener">
            ${post.num_comments} comments
          </a>
        </div>
      </div>
    </li>
  `;
}

function renderPosts(posts) {
  // 1. Post yoxdursa erkən xəta mesajı qaytarırıq
  if (posts.length === 0) {
    setStateMessage("No posts found. Has the pipeline been run yet?");
    return;
  }
  
  // 2. Postlar varsa mesajı təmizləyirik
  setStateMessage("");
  
  // 3. Postları HTML string-ə çevirib birləşdiririk və ekrana basırıq
  const html = posts.map((post, index) => buildPostHTML(post, index + 1)).join("");
  postListEl.innerHTML = html;
}

// ============================================================
// DATA FETCHING
// ============================================================

async function fetchTopPosts() {
  // 1. Yüklənmə mesajını aktiv edirik
  setStateMessage("Loading posts...");
  
  // 2. Try-catch bloku daxilində API-yə sorğu atırıq
  try {
    const response = await fetch(`${API_BASE_URL}/api/posts/top?limit=10`);
    
    // Server cavabı uğurlu deyilsə xəta atırıq
    if (!response.ok) {
      throw new Error(`Server responded with status ${response.status}`);
    }
    
    const result = await response.json();
    
    // Server tərəfindən 'success' statusu yoxlanılır
    if (result.success) {
      renderPosts(result.data);
    } else {
      setStateMessage(result.error || "Something went wrong.", true);
    }
  } catch (error) {
    console.error(error);
    setStateMessage("Could not reach the API. Is the backend server running on port 5000?", true);
  }
}

// ============================================================
// RUN ON PAGE LOAD
// ============================================================

fetchTopPosts();
