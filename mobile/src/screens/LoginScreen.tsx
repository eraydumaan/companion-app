import React, { useState } from "react";
import { View, Text, TextInput, Button, Alert } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { login } from "@/services/api";

export default function LoginScreen({ navigation }: any) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async () => {
    try {
      const { access_token } = await login(email, password);
      await AsyncStorage.setItem("token", access_token);
      navigation.replace("Home");
    } catch (e: any) {
      Alert.alert("Hata", e?.response?.data?.detail || "Giriş başarısız");
    }
  };

  return (
    <View style={{ flex: 1, justifyContent: "center", padding: 16 }}>
      <Text style={{ fontSize: 28, marginBottom: 20 }}>Giriş</Text>
      <TextInput
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        style={{ borderWidth: 1, padding: 10, marginBottom: 12 }}
        autoCapitalize="none"
      />
      <TextInput
        placeholder="Şifre"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
        style={{ borderWidth: 1, padding: 10, marginBottom: 12 }}
      />
      <Button title="Giriş Yap" onPress={onLogin} />
      <View style={{ height: 12 }} />
      <Button title="Kayıt Ol" onPress={() => navigation.navigate("Register")} />
    </View>
  );
}
