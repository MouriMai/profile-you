package models

import (
	"gorm.io/gorm"
)

type Keyword struct {
	gorm.Model
	ID          int    `json:"id`
	Word        string `json:"word`
	Description string `json:"description`
	ImageUrl    string `json:"image_url`
}
