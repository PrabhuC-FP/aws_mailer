<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

class AwsMailController extends Controller
{
    public function send(Request $request)
    {
        $to = $request->input('to', 'recipient@example.com');
        $subject = $request->input('subject', 'Test Email from Laravel');
        $bodyHtml = $request->input('body', '<h1>Hello from Laravel</h1>');
        $sender = $request->input('sender', 'verified@example.com');

        $scriptPath = base_path("storage/python/send_mail.py");

        $process = new Process([
            'env',
            'AWS_ACCESS_KEY_ID=' . env('AWS_ACCESS_KEY_ID'),
            'AWS_SECRET_ACCESS_KEY=' . env('AWS_SECRET_ACCESS_KEY'),
            'AWS_REGION=' . env('AWS_REGION', 'us-west-2'),
            'python3',
            $scriptPath,
            $to,
            $subject,
            $bodyHtml,
            $sender
        ]);
        $process->run();

        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }

        return response()->json([
            'status' => 'success',
            'output' => $process->getOutput()
        ]);
    }
}
