# AppGenStudio - Integrated Development Environment (IDE)

AppGen হলো একটি শক্তিশালী এবং সম্পূর্ণ বাংলা ভাষায় সমর্থিত Android IDE (ইন্টিগ্রেটেড ডেভেলপমেন্ট এনভায়রনমেন্ট) যা বিশেষভাবে বাংলাদেশী ডেভেলপারদের জন্য ডিজাইন করা হয়েছে। এটি MangoSoftBD দ্বারা উন্নয়নকৃত একটি ওপেন সোর্স প্রজেক্ট যা Android অ্যাপ ডেভেলপমেন্টকে আরও সহজলভ্য এবং স্থানীয়কৃত করার লক্ষ্যে তৈরি করা হয়েছে।

📱AppGen এর মাধ্যমে বাংলাদেশী ডেভেলপাররা তাদের মাতৃভাষা বাংলায় কোড লিখতে, ডিবাগ করতে এবং সম্পূর্ণ অ্যাপ্লিকেশন ডেভেলপমেন্ট সাইকেল পরিচালনা করতে পারবেন। এই IDEটি বাংলা UI, বাংলা ডকুমেন্টেশন, বাংলা কোড কমেন্ট এবং বাংলাদেশী SDK সমর্থন সহ সম্পূর্ণ বাংলা অভিজ্ঞতা প্রদান করে।
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="resources/icons/logo_dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="resources/icons/logo_light.svg">
    <img alt="AppGenStudio Logo" src="resources/icons/logo_light.svg" width="400">
  </picture>
</div>

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyQt](https://img.shields.io/badge/PyQt-5.15-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Android](https://img.shields.io/badge/Android-Development-brightgreen)
![Language](https://img.shields.io/badge/Language-EN__US%20%7C%20BN__BD-orange)

একটি সম্পূর্ণ ইনটিগ্রেটেড ডেভেলপমেন্ট এনভায়রনমেন্ট (IDE) যা প্রোগ্রামারদের জন্য কোড লেখা, সম্পাদনা, কম্পাইল এবং ডিবাগ করার একটি সহজ এবং কার্যকর পরিবেশ প্রদান করে। Android ডেভেলপমেন্টের জন্য বিশেষায়িত সমর্থন সহ।

## 📦 Features

- **📝 Code Editor**: সিনট্যাক্স হাইলাইটিং, অটো-কমপ্লিশন এবং কোড ফোল্ডিং সহ উন্নত টেক্সট এডিটর
- **🔧 Compiler Integration**: একাধিক প্রোগ্রামিং ভাষার জন্য কম্পাইলার সাপোর্ট (Python, Java, C++, Android)
- **🐛 Debugger**: ব্রেকপয়েন্ট, ভেরিয়েবল ইনস্পেকশন এবং স্টেপ-থ্রু ডিবাগিং
- **📁 Project Management**: প্রোজেক্ট এক্সপ্লোরার এবং ফাইল ম্যানেজমেন্ট
- **🎨 Customizable UI**: ডার্ক এবং লাইট থিম সাপোর্ট
- **⚡ Performance**: দ্রুত এবং হালকা ওয়েট IDE সলিউশন
- **🌐 Multi-language**: ইংরেজি (EN-US) এবং বাংলা (BN-BD) ভাষা সমর্থন
- **🤖 Android Support**: Android অ্যাপ ডেভেলপমেন্টের জন্য বিশেষ টুলস
- **🌓 Auto Theme Detection**: স্বয়ংক্রিয় ডার্ক/লাইট মোড সনাক্তকরণ

## 🛠 Installation

### Prerequisites
- Python 3.8 বা তার উপরের ভার্সন
- pip (Python package manager)
- Android SDK (Android development এর জন্য)

### Installation Steps

1. **Repository Clone করুন**:
```bash
git clone https://github.com/MangoSoftBD/AppGenStudio.git
cd AppGenStudio
```

2. **Virtual Environment তৈরি করুন** (ঐচ্ছিক):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **ডিপেন্ডেন্সি ইন্সটল করুন**:
```bash
pip install -r requirements.txt
```

4. **Android SDK সেটআপ করুন** (ঐচ্ছিক - Android development এর জন্য):
```bash
# Windows
scripts\install_android_sdk.bat

# Linux/macOS
chmod +x scripts/install_android_sdk.sh
./scripts/install_android_sdk.sh
```

5. **এপ্লিকেশন রান করুন**:
```bash
python src/main.py
```

## 🎨 Theme System

AppGenStudio একটি উন্নত থিম সিস্টেম নিয়ে আসে:

### স্বয়ংক্রিয় থিম সনাক্তকরণ
- সিস্টেমের থিম অনুসারে স্বয়ংক্রিয়ভাবে ডার্ক/লাইট মোড স্যুইচ
- লোগো স্বয়ংক্রিয়ভাবে থিম অনুযায়ী পরিবর্তন হয়

### ম্যানুয়াল থিম সেটিং
```python
# Settings → Preferences → Appearance → Theme
# Available options:
# - "auto" (সিস্টেম থিম অনুসরণ)
# - "dark" (ডার্ক মোড)
# - "light" (লাইট মোড)
```

### লোগো ফাইল স্ট্রাকচার
```
resources/
├── icons/
│   ├── logo_dark.svg     # ডার্ক থিমের জন্য লোগো
│   ├── logo_light.svg    # লাইট থিমের জন্য লোগো
│   ├── icon_dark.png     # ডার্ক থিম অ্যাপ আইকন
│   └── icon_light.png    # লাইট থিম অ্যাপ আইকন
└── themes/
    ├── dark_theme.qss    # ডার্ক থিম স্টাইলশীট
    └── light_theme.qss   # লাইট থিম স্টাইলশীট
```

## 🚀 Usage

### Starting the IDE
```bash
cd AppGenStudio
python src/main.py
```

### Language Selection
ইন্টারফেস ভাষা পরিবর্তন করতে:
1. Settings Menu → Preferences → Language
2. English (EN-US) বা Bengali (BN-BD) সিলেক্ট করুন
3. Apply এবং Restart করুন

### Theme Selection
থিম পরিবর্তন করতে:
1. Settings Menu → Preferences → Appearance
2. Auto, Dark, বা Light সিলেক্ট করুন
3. Apply ক্লিক করুন

### Creating a New Android Project
1. File Menu → New Project → Android Project
2. প্রোজেক্টের নাম এবং লোকেশন সিলেক্ট করুন
3. Target Android version সিলেক্ট করুন
4. Create বাটনে ক্লিক করুন

## 📁 Project Structure

```
AppGenStudio/
├── src/
│   ├── core/
│   ├── gui/
│   │   ├── themes/          # থিম ম্যানেজমেন্ট
│   │   │   ├── theme_manager.py
│   │   │   └── theme_detector.py
│   │   └── ...
│   ├── utils/
│   ├── android/
│   └── main.py
├── resources/
│   ├── icons/
│   │   ├── logo_dark.svg    # ডার্ক থিম লোগো
│   │   ├── logo_light.svg   # লাইট থিম লোগো
│   │   ├── icon_dark.png    # ডার্ক থিম আইকন
│   │   └── icon_light.png   # লাইট থিম আইকন
│   ├── themes/
│   │   ├── dark_theme.qss   # ডার্ক থিম স্টাইল
│   │   └── light_theme.qss  # লাইট থিম স্টাইল
│   └── translations/
├── tests/
├── docs/
├── config/
└── scripts/
```

## 🧪 Testing

থিম সিস্টেম টেস্ট:
```bash
pytest tests/test_themes.py
```

সব টেস্ট রান করুন:
```bash
pytest tests/
```

## 📦 Building

থিম সাপোর্ট সহ executable বানানোর জন্য:
```bash
python scripts/build.py
```

## 🌓 Theme Configuration

### config/settings.json
```json
{
  "appearance": {
    "theme": "auto",
    "icon_theme": "auto",
    "font_size": 14,
    "font_family": "Consolas"
  }
}
```

### থিম ম্যানেজমেন্ট কোড
```python
# src/gui/themes/theme_manager.py
class ThemeManager:
    def __init__(self):
        self.current_theme = "auto"
        self.dark_theme = "resources/themes/dark_theme.qss"
        self.light_theme = "resources/themes/light_theme.qss"
    
    def detect_system_theme(self):
        # সিস্টেম থিম ডিটেকশন লজিক
        pass
    
    def load_theme(self, theme_name):
        # থিম লোড করার লজিক
        pass
    
    def get_logo_path(self):
        # বর্তমান থিম অনুযায়ী লোগো পাথ রিটার্ন
        if self.current_theme == "dark":
            return "resources/icons/logo_dark.svg"
        else:
            return "resources/icons/logo_light.svg"
```

## 🤝 Contributing

আমরা নতুন থিম এবং লোগো ডিজাইনে অবদানকে স্বাগত জানাই:

1. `resources/themes/` এ নতুন থিম ফাইল যোগ করুন
2. `resources/icons/` এ লোগো এবং আইকন যোগ করুন
3. Pull Request জমা দিন

## 📄 License

MIT License - বিস্তারিত জানতে [LICENSE](LICENSE) ফাইল দেখুন।

## 👨‍💻 Developer

**Ashikur Rahaman**  
- 📧 Email: [mangolabbd@outlook.com](mailto:mangolabbd@outlook.com)
- 📱 Mobile: +8801719081545
- 🏢 Company: [MangoSoftBD](https://github.com/MangoSoftBD)
- 📍 Address: Kalkini, Madaripur-7920, Dhaka, Bangladesh

---

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="resources/icons/logo_dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="resources/icons/logo_light.svg">
    <img alt="AppGenStudio Logo" src="resources/icons/logo_light.svg" width="200">
  </picture>
  <br>
  <strong>Light and Dark Theme Support</strong>
</div>
