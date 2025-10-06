import React from "react";
import { View, Text, Button, Alert } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";

export default function HomeScreen({ navigation }: any) {
  const logout = async () => {
    await AsyncStorage.removeItem("token");
    Alert.alert("Çıkış yapıldı!");
    navigation.replace("Login");
  };

  return (
    <View style={{ flex: 1, justifyContent: "center", padding: 16 }}>
      <Text style={{ fontSize: 24, marginBottom: 20 }}>Hoş geldin! 🎉</Text>
      <Button title="Çıkış Yap" onPress={logout} />
    </View>
  );
}
