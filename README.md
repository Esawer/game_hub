# 🎮 GameHub

[![Polish](https://img.shields.io/badge/Język-Polski-red)](#pl)
[![English](https://img.shields.io/badge/Language-English-blue)](#en)

---

<a id="pl"></a>
## 🔴 Wersja Polska 🔴
Kolekcja prostych gier napisanych w Pythonie.  
Projekt w przyszłości przejdzie transformację z zestawu narzędzi konsolowych (CLI) do pełnoprawnej platformy webowej.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Requests](https://img.shields.io/badge/Requests-FF6F00?style=for-the-badge&logo=python-requests&logoColor=white)

### 🤖 Użycie AI
Użyłem AI (Gemini) przy tworzeniu tego projektu.  
Pomogło mi z modułem requests i logiką gier.

### 🕹️ Dostępne Gry
Gry zostały zaprojektowane z wykorzystaniem **programowania obiektowego (OOP)**.

| Gra | Opis Techniczny | Wykorzystane Moduły / API |
| :--- | :--- | :--- |
| **Battleships** | Gra w statki z systemem współrzędnych i walidacją trafień. | `random` |
| **Hangman** | Klasyczny wisielec pobierający losowe hasła z sieci. | `requests`, [Random Word API] |
| **Tic Tac Toe** | Kółko i krzyżyk z obsługą dynamicznych plansz (3x3 do 8x8). | `copy` (deepcopy), `re` |
| **Word Chain** | Słowotok sprawdzający poprawność słów w czasie rzeczywistym. | `requests`, [Dictionary API] |

**Przykłady gier - `Word Chain` i `Hangman`:** <p align="center">
![Animationa1](https://github.com/user-attachments/assets/5bbcbce0-4b54-467f-840e-17f0411531f4)
![Animationa2](https://github.com/user-attachments/assets/715467d2-3912-40b6-bb5a-7176ec62edda)
</p>

### 🚀 Przyszła rozbudowa
Projekt ewoluuje w stronę nowoczesnej aplikacji webowej:
- [ ] **Backend:** Migracja logiki gier do frameworka **Django**.
- [ ] **Baza Danych:** Implementacja **PostgreSQL** do zapisu profili graczy i globalnych rankingów.
- [ ] **Multiplayer:** Rozgrywka w czasie rzeczywistym.
- [ ] **Komunikacja:** Zintegrowany czat dla graczy.

---
<a id="en"></a>
## 🔵 English Version 🔵
Collection of simple CLI games, written in Python.  
In the future, this project will evolve into a full-fledged web platform.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Requests](https://img.shields.io/badge/Requests-FF6F00?style=for-the-badge&logo=python-requests&logoColor=white)

### 🤖 AI Usage
I have used AI (Gemini) during the creation of this project.  
It assisted me with the requests module and game logic.

### 🕹️ Available Games
Games were created with **object-oriented programming (OOP)**.

| Game | Description | Modules / API |
| :--- | :--- | :--- |
| **Battleships** | CLI battleships game. | `random` |
| **Hangman** | Classic hangman, where the word is chosen by API. | `requests`, [Random Word API] |
| **Tic Tac Toe** | Tic tac toe with a custom mode (3x3 to 8x8). | `copy` (deepcopy), `re` |
| **Word Chain** | Users have to write a word that starts with the same letter as the last character of the previous word. | `requests`, [Dictionary API] |

**Gameplay examples - `Word Chain` and  `Hangman`:** <p align="center">
![Animationa1](https://github.com/user-attachments/assets/5bbcbce0-4b54-467f-840e-17f0411531f4)
![Animationa2](https://github.com/user-attachments/assets/715467d2-3912-40b6-bb5a-7176ec62edda)
</p>

### 🚀 Future Roadmap
Future evolution of this project:
- [ ] **Backend:** Migration to the **Django** framework.
- [ ] **Database:** Implementation of **PostgreSQL** for account creation and leaderboards.
- [ ] **Multiplayer:** Implementation of online multiplayer.
- [ ] **Communication:** Chat between players.
