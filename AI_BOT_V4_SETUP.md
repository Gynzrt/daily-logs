# AI Bot v4.0 - Setup Guide

## Gemini AI Integration

Bot v4.0 sử dụng **Gemini 2.5 Flash** để tạo nội dung thực sự có giá trị!

## Setup GitHub Secret

**QUAN TRỌNG**: Cần setup Gemini API Key làm GitHub Secret

### Bước 1: Vào GitHub Repository Settings

1. Mở repo: https://github.com/Gynzrt/daily-logs
2. Click **Settings** (tab trên cùng)
3. Sidebar trái: Click **Secrets and variables** → **Actions**

### Bước 2: Thêm Secret

1. Click **New repository secret**
2. Name: `GEMINI_API_KEY`
3. Value: `AIzaSyBe5I96dA0ue48cYJWgP-6cEO6wJnKjRYI`
4. Click **Add secret**

### Bước 3: Verify

- Secret sẽ hiện trong danh sách như: `GEMINI_API_KEY`
- Không thể xem lại value (bảo mật)

## Workflow Files

Bot có 3 workflows:

1. `daily-commit.yml.disabled` - Bot cũ v2.0 (đã disable)
2. `enhanced-daily.yml` - Bot v3.0 template mode
3. `ai-bot-v4.yml` - **Bot v4.0 AI-powered** ⭐

## Chạy Bot v4.0

### Option 1: Tự động (Recommended)

Bot sẽ tự chạy theo schedule:
- 09:00 UTC (16:00 VN)
- 14:00 UTC (21:00 VN)
- 18:00 UTC (01:00 VN)
- 22:00 UTC (05:00 VN)

### Option 2: Manual Trigger

1. Vào: https://github.com/Gynzrt/daily-logs/actions
2. Click workflow "AI-Powered Bot v4.0 (Gemini)"
3. Click "Run workflow"
4. Click "Run workflow" (confirm)

## Theo dõi Logs

1. Vào Actions tab
2. Click vào workflow run mới nhất
3. Click vào job "ai-bot"
4. Xem logs từng step

## Features v4.0

### AI-Generated Content

**Learning Notes:**
- AI giải thích technical concepts
- 200-250 words mỗi note
- Practical examples
- Key takeaways

**Coding Challenges:**
- Daily algorithm problems
- Complete solutions with comments
- Time/Space complexity analysis
- Detailed explanations

### Smart Patterns

- **Weekday**: 3-5 commits/day
- **Weekend**: 1-3 commits/day
- **Skip days**: 5% chance (simulate vacation)
- **Random delays**: 0-30 minutes

### Content Quality

✅ Real educational value
✅ Unique AI-generated content
✅ Professional explanations
✅ Not spam, actually useful!

## Troubleshooting

### Bot không chạy?

**Check 1: GitHub Secret**
```
Settings → Secrets → GEMINI_API_KEY phải tồn tại
```

**Check 2: Workflow enabled**
```
Actions tab → "AI-Powered Bot v4.0" phải enabled
```

**Check 3: API Quota**
```
Gemini free tier: 1500 requests/day
Bot chỉ dùng 4-8 requests/day → OK!
```

### Content không có AI?

Check logs xem có dòng:
```
AI Mode: ENABLED (Gemini 2.5 Flash)
```

Nếu thấy:
```
AI Mode: DISABLED (fallback to templates)
```

→ API key không work, check lại secret

## Cost Estimate

**Gemini 2.5 Flash (Free Tier):**
- Quota: 1500 requests/day
- Bot usage: 4-8 requests/day
- Cost: **$0/month** (hoàn toàn FREE!)

**Pro plan** (nếu cần):
- $0.000075/1K input tokens
- $0.0003/1K output tokens
- ~$0.01-0.05/day = **$0.30-1.50/month**

## Next Steps

1. ✅ Setup GitHub Secret (GEMINI_API_KEY)
2. ✅ Commit và push v4.0 code
3. ✅ Trigger manual test run
4. ✅ Verify AI content được tạo
5. ✅ Enjoy automated learning! 🎉

---

**Bot v4.0**: Real AI, Real Learning, Real Value! 🚀
