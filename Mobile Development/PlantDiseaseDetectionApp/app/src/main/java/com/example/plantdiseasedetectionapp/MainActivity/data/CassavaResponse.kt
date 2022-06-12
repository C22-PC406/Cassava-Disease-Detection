package com.example.plantdiseasedetectionapp.MainActivity.data

import com.google.gson.annotations.SerializedName

data class CassavaResponse(

	@field:SerializedName("confidence")
	val confidence: Double? = null,

	@field:SerializedName("class")
	val jsonMemberClass: String? = null
)
