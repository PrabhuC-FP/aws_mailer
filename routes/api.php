<?php

use Illuminate\Http\Request;
use App\Http\Controllers\AwsMailController;
use Illuminate\Support\Facades\Route;

Route::post('/send-aws-mail', [AwsMailController::class, 'send']);
