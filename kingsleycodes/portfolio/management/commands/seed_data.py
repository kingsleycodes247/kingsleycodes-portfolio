from django.core.management.base import BaseCommand
from portfolio.models import Service, FAQ, Project

SERVICES = [
    {
        'title': 'Mobile Development',
        'short': 'Android, Kotlin, Java, React Native apps.',
        'long': 'Native Android (Java/Kotlin) and cross-platform (React Native) mobile apps with payments and offline sync.',
        'faqs': [
            {'q': 'Do you build native apps?', 'a': 'Yes — Android using Java/Kotlin; I also work with React Native for cross-platform apps.'},
            {'q': 'Can you integrate payments?', 'a': 'Yes — REST API integrations, stripe, mobile money and crypto payments.'},
        ],
    },
    {
        'title': 'Web Development',
        'short': 'Django, React, Angular, Node, REST APIs.',
        'long': 'Full-stack web applications with Django backends and modern frontends (React/Next/Tailwind).',
        'faqs': [
            {'q': 'What stacks do you use?', 'a': 'Django REST, React, Angular, Node, Tailwind CSS, PostgreSQL.'},
            {'q': 'Can you deploy to production?', 'a': 'Yes — I deploy to AWS, PythonAnywhere, Render, and servers with CI/CD.'},
        ],
    },
    {
      'title': 'Desktop Development',
      'short': 'Java desktop apps, Python GUI tools.',
      'long': 'Desktop utilities and internal tools with Java & Python (Tkinter/ttkbootstrap).',
      'faqs': [
        {'q': 'Which platforms?', 'a': 'Primarily Windows and cross-platform Java-based apps.'},
      ],
    },
    {
      'title': 'DevOps & Cloud Engineering',
      'short': 'CI/CD, Docker, automation, server deployments.',
      'long': 'Automated deployments, Docker, monitoring, and scalable infrastructure design.',
      'faqs': [
        {'q': 'Do you manage cloud infra?', 'a': 'Yes—setup CI/CD, Docker containers, and monitor production systems.'},
      ],
    },
    {
      'title': 'Blockchain Engineering',
      'short': 'Solana, wallets, token integrations.',
      'long': 'Crypto wallets, Solana SPL tokens, secure transaction integrations and blockchain API work.',
      'faqs': [
        {'q': 'Which chains?', 'a': 'Solana (SPL) primarily, Ethereum (ETH) and Bitcoin (BTC) with wallet integrations and secure transaction design.'},
      ],
    },
    {
      'title': 'AI & Automation',
      'short': 'Automation pipelines and AI-assisted features.',
      'long': 'Automation with Celery + Redis, and AI integrations for data processing and alerts.',
      'faqs': [
        {'q': 'Do you build AI pipelines?', 'a': 'Yes — I integrate ML/AI services for automation and real-time alerts.'},
      ],
    },
    {
      'title': 'S.E.O & Digital Marketing',
      'short': 'SEO, performance, content strategy.',
      'long': 'On-page SEO improvements, performance optimization, and content-driven organic growth.',
      'faqs': [
        {'q': 'Can you improve page speed?', 'a': 'Yes — optimizations for server, assets, and frontend for better SEO.'},
      ],
    },
    {
      'title': 'Creative Studio Design',
      'short': 'UI/UX, branding, Canva designs, video editing.',
      'long': 'UI/UX, brand identity, marketing visuals and short-form videos (Reels/Shorts) using Canva and other tools.',
      'faqs': [
        {'q': 'What deliverables?', 'a': 'UI prototypes, branding packages, social media short videos and thumbnails.'},
      ],
    },
    {
      'title': 'Technical Writing',
      'short': 'Project reports, documentation & research writing.',
      'long': 'Technical reports, design docs, and user manuals written to professional standards.',
      'faqs': [
        {'q': 'Do you write project reports?', 'a': 'Yes — I produce detailed technical and business reports.'},
      ],
    },
]

PROJECTS = [
    {
        'title': 'Price Sentinel',
        'description': 'Real-time crypto alert app built with Django, Celery, and Redis.',
        'image': 'projects/price-sentinel.png',
        'link': 'https://github.com/kingsleycodes247/price-sentinel'
    },
    {
        'title': 'Akpa Wallet',
        'description': 'Mobile fintech wallet with secure transactions built with Android and Spring Boot.',
        'image': 'projects/akpa-wallet.png',
        'link': 'https://github.com/kingsleycodes247/akpa-wallet'
    },
]

class Command(BaseCommand):
    help = 'Seed or update services, FAQs, and projects data.'

    def handle(self, *args, **options):
        # ---- Seed or update services ----
        for s in SERVICES:
            service, created = Service.objects.update_or_create(
                title=s['title'],
                defaults={
                    'description': s['long'],
                    'icon': 'fa-solid fa-code'
                }
            )
            # Manage FAQs
            FAQ.objects.filter(question__in=[f['q'] for f in s.get('faqs', [])]).delete()
            for f in s.get('faqs', []):
                FAQ.objects.update_or_create(
                    question=f['q'],
                    defaults={'answer': f['a']}
                )

            action = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f'{action} service: {service.title}'))

        # ---- Seed or update projects ----
        for p in PROJECTS:
            project, created = Project.objects.update_or_create(
                title=p['title'],
                defaults={
                    'description': p['description'],
                    'image': p['image'],
                    'link': p['link']
                }
            )
            action = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f'{action} project: {project.title}'))

        self.stdout.write(self.style.SUCCESS("✅ Seeding complete (services, FAQs, projects)."))
