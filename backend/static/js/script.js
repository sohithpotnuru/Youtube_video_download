// API Base URL
const API_URL = '/api';

// DOM Elements
const urlInput = document.getElementById('urlInput');
const downloadBtn = document.getElementById('downloadBtn');
const statusMessage = document.getElementById('statusMessage');
const progressBar = document.getElementById('progressBar');
const videosList = document.getElementById('videosList');

// Event Listeners
downloadBtn.addEventListener('click', handleDownload);
urlInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleDownload();
    }
});

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    loadVideos();
    // Refresh videos every 30 seconds
    setInterval(loadVideos, 30000);
});

/**
 * Handle video download
 */
async function handleDownload() {
    const url = urlInput.value.trim();

    if (!url) {
        showMessage('Please enter a YouTube URL', 'error');
        return;
    }

    downloadBtn.disabled = true;
    progressBar.classList.remove('hidden');
    showMessage('Starting download...', 'info');

    try {
        const response = await fetch(`${API_URL}/download`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url }),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Download failed');
        }

        showMessage(
            `✓ Downloaded: ${data.title} (${data.size_mb} MB)`,
            'success'
        );
        urlInput.value = '';
        
        // Reload videos list
        setTimeout(() => {
            loadVideos();
        }, 1000);
    } catch (error) {
        showMessage(`✗ Error: ${error.message}`, 'error');
    } finally {
        downloadBtn.disabled = false;
        progressBar.classList.add('hidden');
    }
}

/**
 * Load and display all downloaded videos
 */
async function loadVideos() {
    try {
        const response = await fetch(`${API_URL}/videos`);

        if (!response.ok) {
            throw new Error('Failed to load videos');
        }

        const videos = await response.json();

        if (videos.length === 0) {
            videosList.innerHTML = `
                <div class="empty-message">
                    <div class="empty-icon">📹</div>
                    <p>No videos downloaded yet</p>
                    <p style="font-size: 0.9rem; color: var(--text-secondary);">
                        Enter a YouTube URL above to get started
                    </p>
                </div>
            `;
            return;
        }

        videosList.innerHTML = videos
            .reverse()
            .map((video) => createVideoCard(video))
            .join('');

        // Add event listeners to delete buttons
        document.querySelectorAll('.delete-btn').forEach((btn) => {
            btn.addEventListener('click', () => {
                const filename = btn.dataset.filename;
                deleteVideo(filename);
            });
        });

        // Add event listeners to download buttons
        document.querySelectorAll('.download-video-btn').forEach((btn) => {
            btn.addEventListener('click', () => {
                const filename = btn.dataset.filename;
                downloadVideoFile(filename);
            });
        });
    } catch (error) {
        console.error('Error loading videos:', error);
        videosList.innerHTML = `
            <div class="empty-message">
                <p>Error loading videos</p>
            </div>
        `;
    }
}

/**
 * Create a video card HTML element
 */
function createVideoCard(video) {
    const safeTitle = video.title
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');

    return `
        <div class="video-card">
            <div class="video-card-thumbnail">🎬</div>
            <h3 class="video-card-title" title="${safeTitle}">${safeTitle}</h3>
            <div class="video-card-info">
                <div class="video-card-size">📦 ${video.size_mb} MB</div>
                <div class="video-card-date">📅 ${video.download_date}</div>
            </div>
            <div class="video-card-actions">
                <button 
                    class="video-btn download-video-btn" 
                    data-filename="${video.filename}"
                    title="Download to your device"
                >
                    ⬇ Download
                </button>
                <button 
                    class="video-btn delete-btn" 
                    data-filename="${video.filename}"
                    title="Delete this video"
                >
                    🗑 Delete
                </button>
            </div>
        </div>
    `;
}

/**
 * Delete a video
 */
async function deleteVideo(filename) {
    if (!confirm('Are you sure you want to delete this video?')) {
        return;
    }

    try {
        const response = await fetch(`${API_URL}/delete/${encodeURIComponent(filename)}`, {
            method: 'DELETE',
        });

        if (!response.ok) {
            throw new Error('Failed to delete video');
        }

        showMessage('✓ Video deleted successfully', 'success');
        loadVideos();
    } catch (error) {
        showMessage(`✗ Error deleting video: ${error.message}`, 'error');
    }
}

/**
 * Download video file
 */
function downloadVideoFile(filename) {
    const downloadUrl = `${API_URL}/download-file/${encodeURIComponent(filename)}`;
    
    // Create a temporary link and trigger download
    const link = document.createElement('a');
    link.href = downloadUrl;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    showMessage('✓ Download started', 'success');
}

/**
 * Show status message
 */
function showMessage(message, type) {
    statusMessage.textContent = message;
    statusMessage.className = `status-message ${type}`;

    // Auto-hide success and info messages after 5 seconds
    if (type !== 'error') {
        setTimeout(() => {
            statusMessage.className = 'status-message';
        }, 5000);
    }
}
