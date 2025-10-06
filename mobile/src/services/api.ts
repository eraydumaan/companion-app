import axios from "axios";

export const api = axios.create({
  baseURL: "http://172.29.64.1:8000", // <--- KENDİ IP ADRESİNİ BURAYA YAZ
  timeout: 5000
});

export async function login(email: string, password: string) {
  const res = await api.post("/auth/login", { email, password });
  return res.data as { access_token: string };
}

export async function register(email: string, password: string, full_name: string) {
  const res = await api.post("/auth/register", { email, password, full_name });
  return res.data;
}
