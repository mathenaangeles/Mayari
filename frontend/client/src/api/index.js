import axios from "axios";

const API_URL = "http://127.0.0.1:5000";

// export function fetchLoans() {
//   return axios.get(`${API_URL}/loans/`, {headers:{ Authorization: `Bearer: ${jwt}`}})
// }

export function login(user) {
  return axios.post(`${API_URL}/users/login/`, user);
}

export function register(user) {
  return axios.post(`${API_URL}/users/register/`, user);
}
