from pydantic import BaseModel, Field
"""
{
  "product_name": "Smoked Beef & Melted Mozzarella Fried Bread",
  "tagline": "Garing di Luar, Lumer di Dalam. Cemilan Sore Sempurna.",
  "marketing_copy": "Hadirkan momen ngemil yang tak terlupakan dengan varian roti goreng premium terbaru kami. Kombinasi sempurna antara tekstur roti yang renyah di luar dan sangat lembut di dalam, berpadu dengan isian smoked beef tebal dan keju mozzarella yang lumer di setiap gigitan. Dibuat khusus untuk menemani waktu santai Anda dan keluarga.",
  "open_po_details": {
    "price": 25000,
    "urgency_text": "Slot Terbatas! Amankan pesanan untuk batch Open PO minggu depan."
  },
  "seo_keywords": [
    "roti goreng premium", 
    "cemilan sore", 
    "smoked beef mozzarella", 
    "open po cemilan", 
    "roti isi daging"
  ],
  "social_media_hashtags": [
    "#RotiGorengPremium", 
    "#CemilanKeluarga", 
    "#OpenPO", 
    "#MozzarellaLumer"
  ]
}
"""
class OpenPODetails(BaseModel):
    """Model for open purchase order details."""
    price: float = Field(..., description="The price of the product in the open purchase order.")
    urgency_text: str = Field(..., description="A message indicating the urgency of the open purchase order.")
    
class LaunchingProductModel(BaseModel):
    """Model for specific product details to be launched."""
    product_id: str = Field(..., description="The unique identifier for the product.")
    name: str = Field(..., description="The name of the product.")
    tagline: str = Field(..., description="A catchy tagline for the product.")
    open_po_details: OpenPODetails = Field(..., description="Details regarding the open purchase order for the product.")
    seo_keywords: list[str] = Field(..., description="A list of SEO keywords associated with the product.")
    social_media_hashtags: list[str] = Field(..., description="A list of social media hashtags for the product.")
