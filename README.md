# 🍕 Food Health Classifier

An AI-powered web application that recognizes food from images and provides nutritional analysis with health scores.

![Food Health Classifier](https://img.shields.io/badge/AI-Food%20Recognition-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![React](https://img.shields.io/badge/React-TypeScript-61dafb)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)

## ✨ Features

- 🔍 **AI Food Recognition** - Identifies 101 different food types using EfficientNet
- 📊 **Nutritional Analysis** - Complete macros breakdown (calories, protein, fat, carbs, sugar)
- 💚 **Health Scoring** - Rates food from 0-10 based on nutritional value
- 📸 **Drag & Drop Upload** - Easy image upload with preview
- 🎨 **Modern UI** - Beautiful, responsive design with smooth animations
- ⚡ **Real-time Processing** - Fast predictions powered by HuggingFace Transformers

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 16+
- Git

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: `http://localhost:8000`

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will be available at: `http://localhost:5173`

## 🎯 How It Works

1. **Upload Image** - Drag & drop or select a food image
2. **AI Analysis** - Model identifies the food using Food-101 trained EfficientNet
3. **Results** - Get food name, confidence score, nutritional breakdown, and health rating

## 🍔 Supported Foods

The model recognizes **101 different food types** including:

- 🍕 Fast Food: Pizza, Burgers, Hot Dogs, French Fries
- 🍝 Italian: Pasta, Lasagna, Risotto, Tiramisu
- 🍣 Asian: Sushi, Ramen, Pad Thai, Dumplings
- 🥗 Healthy: Salads, Grilled Salmon, Edamame
- 🍰 Desserts: Cheesecake, Ice Cream, Chocolate Cake

[See full list of supported foods](FOOD_CLASSES.md)

## 🧠 Model Details

- **Architecture**: EfficientNet-B0 (HuggingFace: `nateraw/food`)
- **Dataset**: Food-101 (101 food categories)
- **Confidence Threshold**: 50% (lower confidence returns "Unknown")
- **Input**: RGB images, auto-resized
- **Output**: Top-5 predictions with confidence scores

## 📊 Tech Stack

### Backend
- **FastAPI** - High-performance Python web framework
- **PyTorch** - Deep learning framework
- **HuggingFace Transformers** - Pre-trained models
- **Pillow** - Image processing

### Frontend
- **React** - UI library
- **TypeScript** - Type safety
- **Vite** - Fast build tool
- **CSS3** - Modern styling with gradients and animations

## 📁 Project Structure

```
food-health-classifier/
├── backend/
│   ├── app.py                 # FastAPI main app
│   ├── routers/
│   │   └── predict.py         # Prediction endpoint
│   ├── utils/
│   │   ├── nutrition_map.py   # Nutritional data (101 foods)
│   │   ├── health_index.py    # Health scoring algorithm
│   │   └── preprocess.py      # Image preprocessing
│   ├── model/
│   │   ├── labels_food101.json
│   │   └── config.json
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload.tsx
│   │   │   ├── ResultCard.tsx
│   │   │   ├── HealthBadge.tsx
│   │   │   └── NutritionChart.tsx
│   │   ├── api/
│   │   │   └── predict.ts
│   │   └── App.tsx
│   └── package.json
└── README.md
```

## 🔮 Future Enhancements

- [ ] Ingredient Recognition (apples, bananas, raw vegetables)
- [ ] Multi-food detection (detect multiple items in one image)
- [ ] Meal planning suggestions
- [ ] User accounts and history
- [ ] Mobile app (React Native)
- [ ] Recipe recommendations

See [SOLUTII_INGREDIENTE.md](SOLUTII_INGREDIENTE.md) for ingredient recognition implementation plans.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Andi Prapugicu**
- GitHub: [@AndiPrapugicu](https://github.com/AndiPrapugicu)

## 🙏 Acknowledgments

- Food-101 Dataset by ETH Zurich
- HuggingFace for pre-trained models
- USDA FoodData Central for nutritional data

---

Made with ❤️ and 🍕
