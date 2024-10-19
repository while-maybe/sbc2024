const { getUserRepos } = require("./github");

// TODO: Enter your GitHub username
const gitHubUser = "while-maybe";

getUserRepos(gitHubUser).then((repos) => {
  console.log(repos);
});
