//% color="#D4AF37" icon="\uf0ad" block="Game Cheats"
namespace gameCheats {
    // This variable is now "private" to this namespace
    let autoBlockerEnabled = false

    /**
     * Prevents enemies from touching the player when active
     */
    //% block="set auto-blocker $on"
    //% on.shadow="toggleOnOff"
    export function setAutoBlock(on: boolean) {
        autoBlockerEnabled = on

        // This loop stays inside the namespace logic
        game.onUpdate(function () {
            if (autoBlockerEnabled) {
                for (let enemy of sprites.allOfKind(SpriteKind.Enemy)) {
                    for (let p of sprites.allOfKind(SpriteKind.Player)) {
                        if (enemy.overlapsWith(p)) {
                            // Apply "Repelling Force"
                            enemy.vx *= -1.2
                            enemy.vy *= -1.2
                            enemy.sayText("REFLECTED!", 200)
                        }
                    }
                }
            }
        })
    }

    /**
     * Set a sprite's speed instantly
     */
    //% block="set $target super speed $speed"
    //% target.shadow="variables_get"
    //% speed.defl=300
    export function superSpeed(target: Sprite, speed: number) {
        target.vx = speed
        target.vy = speed
        controller.moveSprite(target, speed, speed)
    }

    /**
     * Makes a sprite leave a colorful trail
     */
    //% block="rainbow trail $target"
    //% target.shadow="variables_get"
    export function rainbowTrail(target: Sprite) {
        // Corrected effect name for the internal engine
        target.startEffect(effects.confetti)
    }

    /**
     * Change how gravity affects a sprite
     */
    //% block="set gravity for $target to $value"
    //% target.shadow="variables_get"
    //% value.defl=200
    export function setGravity(target: Sprite, value: number) {
        target.ay = value
    }
}