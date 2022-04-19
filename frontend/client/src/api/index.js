import axios from "axios";

const API_URL = process.env.VUE_APP_API_URL;

export function deleteArticle(articleId, jwt) {
  return axios.delete(`${API_URL}/articles/delete/${articleId}/`, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function updateArticle(article, articleId, jwt) {
  return axios.put(`${API_URL}/articles/edit/${articleId}/`, article, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function fetchAllArticles(jwt) {
  return axios.get(`${API_URL}/articles/`, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function fetchArticle(articleId) {
  return axios.get(`${API_URL}/articles/${articleId}/`);
}

export function fetchArticles() {
  return axios.get(`${API_URL}/articles/published/`);
}

export function postArticle(article, jwt) {
  return axios.post(`${API_URL}/articles/`, article, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function updateLoan(loan, jwt) {
  return axios.put(`${API_URL}/loans/edit/${loan.id}/`, loan, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function fetchAllLoans(jwt) {
  return axios.get(`${API_URL}/loans/`, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function fetchLoan(loanId, jwt) {
  return axios.get(`${API_URL}/loans/${loanId}/`, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function fetchLoans(userId, jwt) {
  return axios.get(`${API_URL}/loans/user/${userId}/`, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function postLoan(loan, jwt) {
  return axios.post(`${API_URL}/loans/`, loan, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function uploadProfilePhoto(image, userId, jwt) {
  return axios.put(`${API_URL}/users/upload/photo/${userId}/`, image, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function updateUser(user, userId, jwt) {
  return axios.put(`${API_URL}/users/${userId}/`, user, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function login(user) {
  return axios.post(`${API_URL}/users/login/`, user);
}

export function register(user) {
  return axios.post(`${API_URL}/users/register/`, user);
}
