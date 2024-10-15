document.getElementById("fetchRepos").addEventListener("click", onfetchRepos);

function onfetchRepos() {
  const username = document.getElementById("username").value;

  if (username) {
    // GitHub API endpoint for fetching user repositories
    const url = `https://api.github.com/users/${username}/repos`;

    // Make a GET request to the GitHub API
    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error("GitHub user not found");
        }
        return response.json();
      })
      .then((data) => {
        renderRepos(data);
        renderRepos2(data);
        renderRepos3(data);
      })
      .catch((error) => {
        console.error("Error:", error.message);
      });
  } else {
    console.log("Please enter a GitHub username.");
  }
}

const renderRepos = (repos) => {
  const reposListEl = document.getElementById("repos");
  let html = "";

  // TODO what does this line do?
  // iterate through the repos object using 'repo' as the iteration variable, then for every repo, get the "full_name" property value and concatenate that in the 'html' variable and assign it to innerHTML of reposListEl (the HTML element with ID "repos").
  repos.forEach((repo) => {
    const repoFullName = repo.full_name;

    html += `<li>${repoFullName}</li>`;
  });

  reposListEl.innerHTML = html;
};

const renderRepos2 = (repos) => {
  const reposListEl = document.getElementById("repos2");

  // TODO what does this line do?
  // loop through the index of "repos", extracting the "full_name" property value to the const "repoFullName". Create an "li" element, assign "repoFullName" to the "textContent" property and then append the "li" to "reposListEl" (the HTML element with ID "repos").
  for (let i = 0; i < repos.length; i++) {
    const repoFullName = repos[i].full_name;

    const repoEl = document.createElement("li");
    repoEl.textContent = repoFullName;
    reposListEl.appendChild(repoEl);
  }
};

const renderRepos3 = (repos) => {
  const reposListEl = document.getElementById("repos3");

  // TODO: what does this line do?
  // maps one "repo" object from the "repos" array via an arrow function which takes a "repo" object as an argument and concatenates a new "li" HTML element containing the "full_name" property value to the "InnerHTML" property of "repostListEl" and adds it (line by line) to the HTML element with ID "repos3". Basically maps each JSON object into an "li" element containing the "full_name" property value injecting it into "reposListEl" which corresponds to the HTML element with ID "repos3".
  repos.map((repo) => (reposListEl.innerHTML += `<li>${repo.full_name}</li>`));
};
