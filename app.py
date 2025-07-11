# ✅ About route
@app.get("/", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        request=request, name="shop.html", context={"name": "Maria"}
    )
