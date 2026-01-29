#!/bin/bash

# Deployment script for Google Cloud Platform
# This script helps deploy the portfolio to GCP Cloud Run or App Engine

echo "🚀 Portfolio Deployment Script for GCP"
echo "========================================"
echo ""

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ Error: gcloud CLI is not installed."
    echo "Please install it from: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

echo "✅ gcloud CLI found"
echo ""

# Menu for deployment options
echo "Select deployment target:"
echo "1) Cloud Run (Recommended - Serverless)"
echo "2) App Engine (Standard Environment)"
echo "3) Exit"
echo ""
read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo ""
        echo "📦 Deploying to Cloud Run..."
        echo ""

        read -p "Enter your GCP project ID: " PROJECT_ID
        read -p "Enter the region (e.g., europe-west1): " REGION

        echo ""
        echo "Setting project..."
        gcloud config set project $PROJECT_ID

        echo ""
        echo "Building and deploying to Cloud Run..."
        gcloud run deploy portfolio \
            --source . \
            --platform managed \
            --region $REGION \
            --allow-unauthenticated \
            --memory 512Mi \
            --cpu 1 \
            --max-instances 10

        echo ""
        echo "✅ Deployment complete!"
        ;;

    2)
        echo ""
        echo "📦 Deploying to App Engine..."
        echo ""

        read -p "Enter your GCP project ID: " PROJECT_ID

        echo ""
        echo "Setting project..."
        gcloud config set project $PROJECT_ID

        echo ""
        echo "Deploying to App Engine..."
        gcloud app deploy app.yaml --quiet

        echo ""
        echo "✅ Deployment complete!"
        ;;

    3)
        echo "Exiting..."
        exit 0
        ;;

    *)
        echo "❌ Invalid choice. Exiting..."
        exit 1
        ;;
esac

echo ""
echo "🎉 Your portfolio is now live on Google Cloud Platform!"
echo ""

