import React, { useState } from "react";
import { View, Text, TextInput, Button, Alert } from "react-native";
import { register } from "@/services/api";

export default function RegisterScreen({ navigation }: any) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [fullName, setFullName] = useState("");

  const onRegister = async () => {
    try {
      await register(email, password, fullName);
      Alert.alert("Başarılı", "Kayıt tamamlandı!");
      navigation.replace("Login");
    } catch (e: any) {
      Alert.alert("Hata", e?.response?.data?.detail || "Kayıt başarısız");
    }
  };

  return (
    <View style={{ flex: 1, justifyContent: "center", padding: 16 }}>
      <Text style={{ fontSize: 28, marginBottom: 20 }}>Kayıt Ol</Text>
      <TextInput
        placeholder="Ad Soyad"
        value={fullName}
        onChangeText={setFullName}
        style={{ borderWidth: 1, padding: 10, marginBottom: 12 }}
      />
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
      <Button title="Kayıt Ol" onPress={onRegister} />
    </View>
  );
}
