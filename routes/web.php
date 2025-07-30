<?php

use App\Http\Controllers\AwsMailController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/send-aws-mail', [AwsMailController::class, 'send']);
