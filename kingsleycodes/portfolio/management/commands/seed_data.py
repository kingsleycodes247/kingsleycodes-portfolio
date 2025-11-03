from django.core.management.base import BaseCommand
from django.utils.text import slugify
from portfolio.models import Service, Project
import json


class Command(BaseCommand):
    help = 'Seeds the database with rich service and project data'

    def handle(self, *args, **kwargs):
        services = [
            {
                'title': 'Mobile Development',
                'short': 'Native Android (Java/Kotlin) and cross-platform (React Native) apps.',
                'long': (
                    "I design and build mobile applications that combine aesthetics with functionality. "
                    "From native Android apps written in Kotlin or Java, to cross-platform builds with React Native... "
                    "each solution is crafted for speed, security, and performance. My apps support offline caching, real-time notifications, "
                    "API integrations, and seamless payment systems (Stripe, Mobile Money, Crypto)."
                ),
                'icon': 'fas fa-mobile-alt',
                'image': 'images/services/mobile.webp',
                'faqs': [
                    {"q": "Do you build for iOS too?", "a": "While I primarily build for Android, I also create cross-platform apps using React Native that run on both iOS and Android."},
                    {"q": "Can you integrate in-app purchases?", "a": "Yes, I integrate in-app payments through APIs like Stripe, Flutterwave, or Google Pay."},
                    {"q": "Do your apps support offline mode?", "a": "Absolutely. I implement local storage and sync systems so users can still access key features offline."},
                    {"q": "What’s your approach to app security?", "a": "Apps are built with encrypted storage, secure API calls, and modern authentication practices like JWT or OAuth2."},
                    {"q": "Can you deploy to Play Store?", "a": "Yes, I handle app signing, Play Console setup, and publishing for clients."},
                    {"q": "Do you offer post-launch maintenance?", "a": "Yes, I provide ongoing updates, bug fixes, and feature rollouts after launch."},
                ]
            },
            {
                'title': 'Web Development',
                'short': 'Full-stack web apps using Django, React, and Tailwind CSS.',
                'long': (
                    "From landing pages to enterprise systems, I build web applications using modern frameworks like Django, React, and Tailwind CSS. "
                    "My solutions are scalable, secure, and optimized for SEO and speed... perfect for startups, SaaS platforms, or e-commerce."
                ),
                'icon': 'fas fa-laptop-code',
                'image': 'images/services/web.webp',
                'faqs': [
                    {"q": "Do you build APIs too?", "a": "Yes, I build REST and GraphQL APIs with Django REST Framework and integrate them with modern frontends."},
                    {"q": "Do you handle UI/UX?", "a": "Yes, I use Tailwind and Framer Motion for smooth, modern, and responsive designs."},
                    {"q": "Can you optimize my website speed?", "a": "Definitely. I use caching, minification, and lazy loading for lightning-fast performance."},
                    {"q": "Do you handle domain and hosting?", "a": "Yes, I set up hosting on AWS, Render, or PythonAnywhere, and connect your custom domain."},
                    {"q": "What about CMS integration?", "a": "I integrate headless CMS like Strapi or custom Django Admin dashboards."},
                    {"q": "Can you migrate my old site?", "a": "Yes, I handle data migration, redesign, and SEO preservation seamlessly."},
                ]
            },
            {
                'title': 'DevOps & Cloud Engineering',
                'short': 'Docker, CI/CD, and infrastructure automation.',
                'long': (
                    "I automate deployments, monitor systems, and containerize applications using Docker and CI/CD pipelines. "
                    "From startup MVPs to enterprise clusters, I design cloud environments that scale effortlessly while maintaining cost efficiency."
                ),
                'icon': 'fas fa-cloud',
                'image': 'images/services/devops.webp',
                'faqs': [
                    {"q": "Do you set up CI/CD?", "a": "Yes, I use GitHub Actions, Jenkins, or GitLab CI for automated deployments."},
                    {"q": "Which clouds do you work with?", "a": "AWS, DigitalOcean, and Render... with scalable Dockerized setups."},
                    {"q": "Can you set up monitoring?", "a": "I integrate Prometheus, Grafana, or custom logging dashboards for real-time system visibility."},
                    {"q": "Do you use Infrastructure as Code?", "a": "Yes, I use Docker Compose and Terraform to ensure repeatable environments."},
                    {"q": "Can you improve deployment times?", "a": "Yes, through build caching and parallel pipelines."},
                    {"q": "What about backups?", "a": "Automated backup routines are included as part of every deployment plan."},
                ]
            },
            {
                'title': 'Blockchain Engineering',
                'short': 'Solana, Web3 wallets, and token integrations.',
                'long': (
                    "Blockchain development tailored for scalability and user trust. "
                    "From Solana token creation to secure wallet integrations and crypto payment gateways, "
                    "I build decentralized apps and backend systems with strong encryption and Web3 standards."
                ),
                'icon': 'fas fa-cube',
                'image': 'images/services/blockchain.webp',
                'faqs': [
                    {"q": "Do you develop smart contracts?", "a": "Yes, primarily on Solana, with experience in Ethereum (Solidity)."},
                    {"q": "Can you integrate wallets?", "a": "Yes, I integrate Phantom, MetaMask, and other major wallets."},
                    {"q": "Do you handle NFT marketplaces?", "a": "Yes, I create minting systems and NFT transaction APIs."},
                    {"q": "What languages do you use?", "a": "Rust (for Solana), Python, and JavaScript for full-stack Web3 integration."},
                    {"q": "Is it secure?", "a": "Security is top priority... I follow strict encryption and audit-ready standards."},
                    {"q": "Can you build token-based platforms?", "a": "Yes, from tokenomics modeling to exchange-ready implementations."},
                ]
            },
            {
                'title': 'Creative Studio Design',
                'short': 'Graphic Design, Logo Design, Branding Video Ads, Reels & Shorts.',
                'long': (
                    "Your brand deserves to *look* as powerful as it *feels*. I design visual identities that speak volumes: "
                    "from minimalist logos and 3D intros to motion reels that stop the scroll. Every design is guided by strategy, "
                    "color psychology, and emotion-driven branding that converts."
                ),
                'icon': 'fas fa-paint-brush',
                'image': 'images/services/creative.webp',
                'faqs': [
                    {"q": "Do you design animated reels?", "a": "Yes, short-form motion graphics optimized for social media."},
                    {"q": "Can you handle full brand identity?", "a": "Yes, logo, palette, typography, and visual direction."},
                    {"q": "Do you create ads for TikTok/Instagram?", "a": "Yes, dynamic and visually engaging reels."},
                ]
            },
            {
                'title': 'Technical Writing',
                'short': 'Professional documentation, reports, and proposals.',
                'long': (
                    "I write clear, structured, and technically accurate documentation... from software guides to research reports. "
                    "Each piece blends professionalism with design: charts, infographics, and visuals to ensure clarity and retention."
                ),
                'icon': 'fas fa-file-alt',
                'image': 'images/services/technical.webp',
                'faqs': [
                    {"q": "Do you handle academic reports?", "a": "Yes, structured project reports and proposals."},
                    {"q": "Do you include design elements?", "a": "Yes, I format and style reports in LaTeX, MS Word, or InDesign."},
                    {"q": "Can you document APIs?", "a": "Yes, with schema explanations and example endpoints."},
                ]
            },
            {
                'title': 'Desktop Development',
                'short': 'Python GUI (Tkinter, TTK Bootstrap) and Java applications.',
                'long': (
                    "I build lightweight and secure desktop apps with clean user interfaces using Python Tkinter/TTK Bootstrap or JavaFX. "
                    "Perfect for offline tools, POS systems, and internal business automation."
                ),
                'icon': 'fas fa-desktop',
                'image': 'images/services/desktop.webp',
                'faqs': [
                    {"q": "Do your apps work offline?", "a": "Yes, completely standalone executables."},
                    {"q": "Can you create installer packages?", "a": "Yes, with auto-updates via Inno Setup or PyInstaller."},
                    {"q": "Do you support cross-platform builds?", "a": "Yes, Windows, macOS, and Linux support."},
                ]
            },
            {
                'title': 'Digital Marketing & SEO',
                'short': 'Boosting visibility with strategy, content, and precision targeting.',
                'long': (
                    "I craft digital marketing campaigns powered by psychology and analytics. "
                    "From search optimization and Google Ads to creative video marketing... your brand’s growth becomes measurable and predictable."
                ),
                'icon': 'fas fa-bullhorn',
                'image': 'images/services/digital.webp',
                'faqs': [
                    {"q": "Do you run ad campaigns?", "a": "Yes, Google Ads, Meta Ads, and LinkedIn campaigns."},
                    {"q": "Do you handle SEO?", "a": "Yes, on-page, technical, and content-driven SEO."},
                    {"q": "Can you create content too?", "a": "Yes, blogs, visuals, and video scripts aligned with your strategy."},
                ]
            },
        ]

        Service.objects.all().delete()

        for s in services:
            service, created = Service.objects.get_or_create(
                slug=slugify(s['title']),
                defaults={
                    'title': s['title'],
                    'short': s['short'],
                    'long': s['long'],
                    'icon': s['icon'],
                    'image': s['image'],
                    'faqs': s['faqs']
                }
            )
            self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} service: {service.title}"))

        
        projects = [
            {
                'title': 'Capital Trace Website',
                'description': 'Financial Tracking and Asset recovery services Website.',
                'image': 'images/projects/capitaltrace.webp',
                'link': 'https://www.capitaltrace.net'
            },
            {
                'title': 'Asset Restitution Website',
                'description': 'Social Media, Investment Scam recovery Solutions and Cybersecurity Platform.',
                'image': 'images/projects/assetrestitution.webp',
                'link': 'https://www.assetrestitution.net'
            },
            {
                'title': 'JKGS Solutions Website',
                'description': 'Travel Planning, Visa and Community Services Website.',
                'image': 'images/projects/jkgssolutions.webp',
                'link': 'https://www.jkgssolutions.com'
            },
            {
                'title': 'Shekel Coin Blockchain Token',
                'description': 'Solana network memecoin project with metadata, wallet integration. Built with Solana SPL & TypeScript.',
                'image': 'images/projects/shekel.webp',
                'link': 'https://explorer.solana.com/address/EXGbbSvXLDxJv9Dw397pwgmZ4KEL4r65u3VDZ7pixDDS?cluster=devnet'
            },
            {
                'title': 'Price Sentinel Web Application',
                'description': 'Crypto alert tracker with Django, Celery, and Redis. Notifies users of live market shifts.',
                'image': 'images/projects/pricesentinel.webp',
                'link': 'https://github.com/kingsleycodes247/price-sentinel'
            },
            {
                'title': 'Kings Cuisine Restaurant Website',
                'description': 'Clean and Professional Restaurant Website built with Django, HTML5, CSS3, Bootstrap and JavaScript.',
                'image': 'images/projects/kings.webp',
                'link': 'https://kings-cuisine.onrender.com/'
            },
            {
                'title': 'Akpa Wallet',
                'description': 'Secure Fintech & Crypto android wallet app built with Java and Springboot microservices backend.',
                'image': 'images/projects/akpa.jpeg',
                'link': 'https://play.google.com/store/apps?hl=en&gl=US'
            },
            {
                'title': 'SMK Inventory Desktop App',
                'description': 'Professional Inventory Management System Desktop App built with Python Tkinter, with Real-time email alerts.',
                'image': 'images/projects/smk.webp',
                'link': 'https://drive.google.com/drive/folders/1dwQLVGz-UgSzWsURNtt3HtXOGdfAs8gF?usp=drive_link'
            },
        ]

        Project.objects.all().delete()

        for p in projects:
            project, created = Project.objects.get_or_create(
                slug=slugify(p['title']),
                defaults={
                    'title': p['title'],
                    'description': p['description'],
                    'image': p['image'],
                    'link': p['link']
                }
            )
            self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} project: {project.title}"))

        self.stdout.write(self.style.SUCCESS("✅ Database successfully seeded with rich services and projects."))
